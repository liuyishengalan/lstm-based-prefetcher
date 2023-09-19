# LSTM-based Prefetcher

Embedding LSTM model is implemented in this prefetcher, based on the paper: [Learning Memory Access Patterns](https://arxiv.org/pdf/1803.02329.pdf)

Check the progress [log file]( progress_log.md ) first

Model Structure: 

![model](misc/model.png)

Tested workload: 

- Dhrystone: [source code](https://www.netlib.org/benchmark/dhry-c)
  - Training Accuracy: 100%
  - Validating Accuracy: na%
- Canneal
  - Training Accuracy: na%
  - Validating Accuracy: na%
- Blackscholes
  - Training Accuracy: na%
  - Validating Accuracy: na%
- Ferret
  - Training Accuracy: na%
  - Validating Accuracy: na%
