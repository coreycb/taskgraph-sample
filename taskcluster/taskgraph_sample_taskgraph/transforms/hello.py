from voluptuous import ALLOW_EXTRA, Required

from taskgraph.transforms.base import TransformSequence
from taskgraph.util.schema import Schema

HELLO_SCHEMA = Schema(
    {
        Required("noun"): str,
    },
    extra=ALLOW_EXTRA,
)

# Container for a sequence of transforms. Each transform is represented
# as a callable taking (config, items) and returning a generator which
# will yield transformed items. The resulting sequence has the same
# interface.
#
# This is convenient to use in a file full of transforms, as it provides
# a decorator, @transforms.add, that will add the decorated function to
# the sequence.
transforms = TransformSequence()

transforms.add_validate(HELLO_SCHEMA)


# Add the decorated function to the callable transform sequence
@transforms.add
def add_noun(config, tasks):
    for task in tasks:
        noun = task.pop("noun").capitalize()
        task["description"] = f"Prints 'Hello {noun}'"
        print(f'{task["description"]}')

        env = task.setdefault("worker", {}).setdefault("env", {})
        env["NOUN"] = noun

        yield task
