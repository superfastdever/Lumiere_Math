# Task store

Built to hold well over ten thousand tasks without any directory growing unmanageable.

## Lifecycle

    queue      drafted here, not yet sent for model testing
    testing    handed over, waiting on the two model runs
    passed     both models failed, submitted to the pipeline
    delivered  cleared stage 7, paid
    returned   bounced back from a stage, reason recorded in RETURN.md
    retired    killed before or after testing, reason recorded in RETIRE.md

A task is one directory. It moves between the folders above as its state changes.
`tools/lm.py` performs the move and rewrites the registry in the same step, so the
two never drift apart.

## Sharding

Ten thousand directories in one folder is unusable, so every state folder shards on
the first two digits of the zero padded id:

    tasks/passed/00/t00017/
    tasks/passed/04/t00412/
    tasks/queue/13/t01337/

One hundred shards, so a hundred tasks per shard at ten thousand, and a thousand each
at a hundred thousand. Nothing needs restructuring if the project grows.

## Inside a task directory

    TASK.md      the package: ground truth, solution, description, distractors, analysis
    figure.png   the image, or figure1.png .. figure5.png when several are used
    build/       scripts that generated and verified the figure, kept so any number is reproducible
    PROMPT.md    the author's prompt text, added by the author, never generated here
    MODELS.md    the two model responses, added after testing
    RETURN.md    only in returned/, what came back and from which stage
    RETIRE.md    only in retired/, why it was killed

## Index

    _index/registry.csv       one row per task, the source of truth for state
    _index/fingerprints.tsv   dedup keys, checked before a new task is drafted

Near-duplicate tasks are returned with zero tolerance, so the fingerprint file carries
the subdomain, the object type, the invariant asked for and a structural hash. Check it
before drafting, not after building.
