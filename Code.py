from pyspark.sql.functions import when
from pyspark.ml import Pipeline
import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler, VectorIndexer
from pyspark.ml.regression import RandomForestRegressor, GBTRegressor, DecisionTreeRegressor, GeneralizedLinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

#Read data
df =sparkSession.sql("SELECT * FROM dataframe")

# Lists for numeric and categorical features
numericCols = [c for c, t in df.dtypes if t not in ('string','date')]
categoricalCols  = df.select(list(set(df.columns)-set(num))).columns
