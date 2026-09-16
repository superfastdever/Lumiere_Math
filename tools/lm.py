#!/usr/bin/env python3
"""Task store manager for Project Lumiere maths tasks.

    lm.py new  --subdomain SD --object OBJ --invariant INV [--notes ...]
    lm.py move ID STATE [--reason "..."]
    lm.py check ID
    lm.py stat
    lm.py find [--state S] [--subdomain SD] [--object OBJ] [--invariant INV]
"""
import argparse, csv, datetime, hashlib, os, shutil, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS = os.path.join(ROOT, "tasks")
REG = os.path.join(TASKS, "_index", "registry.csv")
FPR = os.path.join(TASKS, "_index", "fingerprints.tsv")
STATES = ["queue", "testing", "passed", "delivered", "returned", "retired"]
FIELDS = ["id", "state", "subdomain", "failure_mode", "gtfa", "created", "updated", "notes"]

def today():
    return datetime.date.today().isoformat()

def shard(tid):
    return re.sub(r"\D", "", tid)[:2].zfill(2)

def task_dir(tid, state):
    return os.path.join(TASKS, state, shard(tid), tid)

def read_registry():
    if not os.path.exists(REG):
        return []
    with open(REG, newline="") as f:
        return list(csv.DictReader(f))

def write_registry(rows):
    rows.sort(key=lambda r: r["id"])
    with open(REG, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

def read_fingerprints():
    if not os.path.exists(FPR):
        return []
    with open(FPR, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def locate(tid):
    for s in STATES:
        d = task_dir(tid, s)
        if os.path.isdir(d):
            return s, d
    return None, None

# ----------------------------------------------------------------- commands
def cmd_new(a):
    rows = read_registry()
    nums = [int(re.sub(r"\D", "", r["id"]) or 0) for r in rows]
    tid = "t%05d" % ((max(nums) + 1) if nums else 1)

    key = "|".join(x.strip().lower() for x in (a.subdomain, a.object, a.invariant))
    h = hashlib.sha1(key.encode()).hexdigest()[:12]
    for fp in read_fingerprints():
        if fp["structure_hash"] == h:
            print(f"REFUSED: fingerprint collides with {fp['id']}")
            print(f"  {fp['subdomain']} / {fp['object']} / {fp['invariant']}")
            print("  near-duplicate tasks are returned with zero tolerance; change the ask.")
            return 2

    d = task_dir(tid, "queue")
    os.makedirs(os.path.join(d, "build"), exist_ok=True)
    tpl = os.path.join(TASKS, "_templates", "TASK.md")
    if os.path.exists(tpl):
        shutil.copy(tpl, os.path.join(d, "TASK.md"))
    rows.append({"id": tid, "state": "queue", "subdomain": a.subdomain,
                 "failure_mode": a.failure_mode or "", "gtfa": "",
                 "created": today(), "updated": today(), "notes": a.notes or ""})
    write_registry(rows)
    with open(FPR, "a", newline="") as f:
        csv.writer(f, delimiter="\t").writerow(
            [tid, a.subdomain, a.object, a.invariant, h, a.notes or ""])
    print(f"created {tid} at {os.path.relpath(d, ROOT)}")
    return 0

def cmd_move(a):
    if a.state not in STATES:
        print(f"unknown state {a.state}; one of {STATES}"); return 2
    cur, src = locate(a.id)
    if not cur:
        print(f"{a.id} not found"); return 2
    dst = task_dir(a.id, a.state)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(src, dst)
    for stale in (os.path.dirname(src),):
        if os.path.isdir(stale) and not os.listdir(stale):
            os.rmdir(stale)
    if a.reason:
        name = {"returned": "RETURN.md", "retired": "RETIRE.md"}.get(a.state)
        if name:
            with open(os.path.join(dst, name), "a") as f:
                f.write(f"## {today()}: moved to {a.state}\n\n{a.reason}\n\n")
    rows = read_registry()
    for r in rows:
        if r["id"] == a.id:
            r["state"], r["updated"] = a.state, today()
            if a.reason:
                r["notes"] = a.reason.replace("\n", " ")[:160]
    write_registry(rows)
    print(f"{a.id}: {cur} -> {a.state}")
    return 0

def cmd_check(a):
    state, d = locate(a.id)
    if not d:
        print(f"{a.id} not found"); return 2
    fails, warns = [], []
    tp = os.path.join(d, "TASK.md")
    if not os.path.exists(tp):
        fails.append("TASK.md missing")
        text = ""
    else:
        text = open(tp).read()

    figs = sorted(f for f in os.listdir(d) if f.lower().endswith((".png", ".jpg", ".jpeg")))
    if not figs:
        fails.append("no figure (PNG or JPEG) in the task directory")
    if len(figs) > 5:
        fails.append(f"{len(figs)} images, limit is 5")
    for fn in figs:
        if not fn.lower().endswith((".png", ".jpg", ".jpeg")):
            fails.append(f"{fn}: format must be PNG or JPEG")
        try:
            from PIL import Image
            im = Image.open(os.path.join(d, fn))
            if im.mode in ("RGBA", "LA") or "transparency" in im.info:
                fails.append(f"{fn}: has an alpha channel, PNG must be opaque")
            if min(im.size) < 700:
                warns.append(f"{fn}: {im.size[0]}x{im.size[1]} is small for a reviewer")
        except ImportError:
            warns.append("Pillow not installed, image checks skipped")

    m = re.search(r"^\*\*GTFA:\s*(.+?)\*\*", text, re.M)
    if not m:
        fails.append("no line of the form **GTFA: ...** in TASK.md")
    elif len(m.group(1).strip()) > 100:
        fails.append("GTFA exceeds 100 rendered characters")

    desc = re.search(r"^## Image description\s*(.+?)^## ", text, re.M | re.S)
    if not desc:
        fails.append("no '## Image description' section")
    else:
        n = len(desc.group(1).split())
        if n < 200:
            fails.append(f"image description is {n} words, minimum is 200")

    dis = re.search(r"^## Distractors\s*(.+?)^## ", text, re.M | re.S)
    if not dis:
        fails.append("no '## Distractors' section")
    else:
        vals = re.findall(r"^\|\s*([^|]+?)\s*\|", dis.group(1), re.M)
        vals = [v for v in vals if v and not set(v) <= set("- ") and v.lower() != "value"]
        if len(vals) != 5:
            fails.append(f"{len(vals)} distractors found, exactly 5 required")
        if len(set(vals)) != len(vals):
            fails.append("distractors are not all distinct")
        if m and m.group(1).strip() in vals:
            fails.append("a distractor equals the GTFA")
        if "including the GTFA" not in dis.group(1):
            fails.append("required note above the distractor list is missing")

    steps = re.findall(r"^\*\*Step (\d+)\.", text, re.M)
    if len(steps) < 3:
        fails.append(f"{len(steps)} numbered steps, minimum is 3")
    if "—" in text:
        warns.append("TASK.md contains an em dash")

    if state in ("passed", "delivered") and not os.path.exists(os.path.join(d, "PROMPT.md")):
        fails.append("PROMPT.md missing, the author's prompt is required at this state")
    if state in ("passed", "delivered") and not os.path.exists(os.path.join(d, "MODELS.md")):
        fails.append("MODELS.md missing, the two model responses are required at this state")

    print(f"{a.id} [{state}] {os.path.relpath(d, ROOT)}")
    for f in fails:
        print("  FAIL ", f)
    for w in warns:
        print("  warn ", w)
    if not fails:
        print("  all mechanical checks pass")
    return 1 if fails else 0

def cmd_stat(a):
    rows = read_registry()
    if not rows:
        print("registry is empty"); return 0
    print(f"{len(rows)} tasks\n")
    for field in ("state", "subdomain", "failure_mode"):
        counts = {}
        for r in rows:
            counts[r[field] or "(unset)"] = counts.get(r[field] or "(unset)", 0) + 1
        print(f"by {field}:")
        for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"   {v:5d}  {k}")
        print()
    return 0

def cmd_find(a):
    rows = read_registry()
    fps = {f["id"]: f for f in read_fingerprints()}
    for r in rows:
        fp = fps.get(r["id"], {})
        if a.state and r["state"] != a.state: continue
        if a.subdomain and a.subdomain.lower() not in r["subdomain"].lower(): continue
        if a.object and a.object.lower() not in fp.get("object", "").lower(): continue
        if a.invariant and a.invariant.lower() not in fp.get("invariant", "").lower(): continue
        print(f"{r['id']}  {r['state']:<10} {r['subdomain']:<38} "
              f"{fp.get('object',''):<28} {fp.get('invariant',''):<30} gtfa={r['gtfa']}")
    return 0

def main():
    p = argparse.ArgumentParser(prog="lm.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new");  n.set_defaults(fn=cmd_new)
    n.add_argument("--subdomain", required=True); n.add_argument("--object", required=True)
    n.add_argument("--invariant", required=True); n.add_argument("--failure-mode", default="")
    n.add_argument("--notes", default="")
    mv = sub.add_parser("move"); mv.set_defaults(fn=cmd_move)
    mv.add_argument("id"); mv.add_argument("state"); mv.add_argument("--reason", default="")
    c = sub.add_parser("check"); c.set_defaults(fn=cmd_check); c.add_argument("id")
    s = sub.add_parser("stat"); s.set_defaults(fn=cmd_stat)
    f = sub.add_parser("find"); f.set_defaults(fn=cmd_find)
    for k in ("state", "subdomain", "object", "invariant"):
        f.add_argument(f"--{k}", default="")
    a = p.parse_args()
    sys.exit(a.fn(a))

if __name__ == "__main__":
    main()
