# Market-Basket-Analysis-Big-Data-Pipeline
A scalable Big Data analytics pipeline using Apache Spark and Hadoop (HDFS) to discover market basket association rules using the FP-Growth algorithm.
# Market Basket Analysis Using Big Data Pipeline (Hadoop & Spark)

## Project Overview
This project implements a scalable Market Basket Analysis (MBA) pipeline designed to process large-scale retail transaction logs. Utilizing a **5-Zone Architecture**, it extracts frequent itemsets and generates validated association rules to enable data-driven cross-selling and inventory strategies.

## 🛠️ Tech Stack & Architecture
- **Storage:** Hadoop Distributed File System (HDFS) for scalable, fault-tolerant data storage.
- **Processing Engine:** Apache Spark (PySpark) leveraging in-memory computation.
- **AI Algorithm:** FP-Growth (Frequent Pattern Growth) for efficient pattern mining without expensive candidate generation.
- **Visualization:** Power BI for interactive executive dashboards.

## 📊 Core Metrics Defined
- **Support:** Frequency of the itemset in the dataset.
- **Confidence:** Conditional probability that a customer buys Item B given they bought Item A.
- **Lift:** Measures the strength of association. A `Lift > 1` indicates a strong, non-coincidental relationship.

## 🚀 Key Challenges Overcome
1. **Hadoop on Windows Environment:** Resolved local pathing and permissions conflicts by properly configuring `Winutils.exe` and `HADOOP_HOME` environment variables.
2. **Memory & Parallelism Tuning:** Tuned executor memory, cores, and shuffle partitions in Spark to eliminate garbage collection pauses and avoid memory leaks during heavy FP-Growth iterations.

## 🔮 Future Enhancements
- Transition from batch processing to **Real-time Streaming** using Apache Kafka.
- Enhance recommendation intelligence by integrating customer session signals and deep learning embeddings.
