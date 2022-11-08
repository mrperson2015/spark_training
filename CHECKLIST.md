### Architecture

* [ ] KISS
    * Keep It Stupid Simple
* [ ] Peer Review
* [ ] Documentation
    * [ ] Lucid Chart
    * [ ] Wiki

### PLANNING

* [ ] User Stories
* [ ] Tasks Have Time Estimates
* [ ] Peer Review
* [ ] Delivery Date ('estimated start date' + ('total estimated task time' * π))

### IMPLEMENTATION

* [ ] Documentation
    * [ ] README.md
    * [ ] Docstrings
    * [ ] Code
    * [ ] Handlers
* [ ] No ide Warnings
* [ ] No ide Errors
* [ ] No Job Warnings
    * except accepted standard warnings
    * ie: 'Setting default log level to \"WARN\".'
* [ ] No Job Errors
* [ ] Peer Review
* [ ] Audits
    * [ ] Minimum
    * [ ] Job Specific
* [ ] Logging
* [ ] Unit Tests
* [ ] Change Log
* [ ] Copyright

```shell
┌───────────────────┬─────────────────────────────────┬───────────────────────────┐
│ Architecture      │ Planning                        │ Implementation            │
│───────────────────│─────────────────────────────────│───────────────────────────│
│ [ ] KISS          │ [ ] User Storie(s)              │ [ ] Documentation         │
│ [ ] Peer Review   │ [ ] Task(s) Have Time Estimates │   [ ] README.md           │
│ [ ] Documentation │ [ ] Peer Review                 │   [ ] Docstrings          │
│ [ ] Lucid Chart   │ [ ] ¹Delivery Date              │   [ ] Code                │
│ [ ] Wiki          │ [ ] Test Plan                   │   [ ] Handlers            │
│                   │ [ ] Deploy Plan                 │ [ ] No IDE Warnings       │
│                   │ [ ] Support Plan                │ [ ] No IDE Errors         │
│                   │                                 │ [ ] ²No Job Warnings      │
│                   │                                 │ [ ] No Job Errors         │
│                   │                                 │ [ ] Peer Review           │
│                   │                                 │ [ ] Audits                │
│                   │                                 │   [ ] Minimum             │
│                   │                                 │   [ ] Job Specific        │
│                   │                                 │ [ ] Logging               │
│                   │                                 │ [ ] Unit Tests            │
│                   │                                 │ [ ] Change Log            │
│                   │                                 │ [ ] Black Formatter       │
│                   │                                 │ [ ] Copyright             │
└───────────────────┴─────────────────────────────────┴───────────────────────────┘
```

¹ 'estimated start date' + ('total estimated task time' * π)<br>
² except accepted standard warnings. (ie 'Setting default log level to "WARN".')