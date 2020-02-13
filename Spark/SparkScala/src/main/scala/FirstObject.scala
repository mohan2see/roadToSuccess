import org.apache.spark.sql.types.{StringType, LongType, StructField, StructType}
import org.apache.spark.sql.{Row, SparkSession}

object FirstObject {

  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder().appName("FirstSParkProg").master("local[*]").getOrCreate()

    val a = spark.range(1000).toDF()
    a.show(10)

    import spark.implicits._
    val b = Seq(Row("Hello", null, 3L))
    val mySchema = new StructType(Array( new StructField("col1", StringType, true), new StructField("col2", StringType, true), new StructField("col3", LongType, true)))
    val c = spark.sparkContext.parallelize(b)
    val df = spark.createDataFrame(c, mySchema)
    df.show()


    val myManualSchema = new StructType(Array(  new StructField("some", StringType, true),  new StructField("col", StringType, true),  new StructField("names", LongType, false)))
    val myRows = Seq(Row("Hello", null, 1L))
    val myRDD = spark.sparkContext.parallelize(myRows)
    val d = spark.createDataFrame(myRDD, myManualSchema)
    d.show()


  }

}
