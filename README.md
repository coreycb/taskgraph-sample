# taskgraph-sample

### setup
```
python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install taskcluster-taskgraph
export PATH=$PATH:.
```

### execute
```
taskgraph init  # Don't run. Was run first on initial creation.
taskgraph full  # Show the full task graph
```
