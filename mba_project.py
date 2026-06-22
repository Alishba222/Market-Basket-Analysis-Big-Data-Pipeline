import os
from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import functions as F

# Step 1: Set environment to avoid Python version errors
os.environ['PYSPARK_PYTHON'] = 'python'

# Step 2: Start Spark Session
spark = SparkSession.builder \
    .appName("Creovata_MBA_Final") \
    .enableHiveSupport() \
    .getOrCreate()

# Step 3: Load data directly from local path
print("\n--- Loading data from Local Path ---")
path = r"C:\Users\FC Technologies\Downloads\Compressed\archive\Groceries_dataset.csv"
df = spark.read.csv(path, header=True, inferSchema=True) \
    .select("Member_number", "ItemDescription")

# Step 4: Group items into "Baskets"
baskets = df.groupBy("Member_number").agg(F.collect_set("ItemDescription").alias("items"))

# Step 5: Train the FP-Growth Model
print("--- AI is training and finding patterns (please wait)... ---")
fpGrowth = FPGrowth(itemsCol="items", minSupport=0.01, minConfidence=0.2)
model = fpGrowth.fit(baskets)

# Step 6: Show the Association Rules in Terminal
print("\n--- MARKET BASKET ANALYSIS RESULTS (Patterns Found) ---")
# Store rules in a variable to use later
final_results = model.associationRules
final_results.show()

# Step 7: Convert Arrays to Strings and Save to CSV (YE PART UPDATE KIYA HAI)
output_path = "C:/Users/FC Technologies/Desktop/Big Data Project/output_results"

print(f"--- Formatting and saving results to CSV at: {output_path} ---")

# Converting 'antecedent' and 'consequent' from Array to String for CSV compatibility
final_csv_data = final_results.withColumn("antecedent", F.concat_ws(", ", F.col("antecedent"))) \
                             .withColumn("consequent", F.concat_ws(", ", F.col("consequent")))

# Now saving to CSV with overwrite mode to avoid folder errors
final_csv_data.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(output_path)

print(f"\n--- Mubarak Ho! CSV file successfully saved. ---")

# Step 8: Keep window open to see results
input("\n>>> RESULTS ARE ABOVE. Press Enter to close this window...")

spark.stop()