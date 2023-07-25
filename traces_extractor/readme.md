### Generate traces

- Intel Pin Tool is used to get memory traces

  - ```
    $pintool/source/yools/ManualExamples/pinatrace.so
    ```

  - ```
    ../../../pin -t obj-intel64/pinatrace.so -- $workload_bin
    ```

  - It will generate pinatrace.out, copy to the folder, traces_extractor

- Execute the shell script: 

  ```
  bash ./gentrace.sh
  ```

  - A csv file will be saved in the folder traces_extractor, named as `traces.csv`.
  - Copy `trace.csv` to the repo folder to allow the model to be trained and validated using the traces.