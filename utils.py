x = (
    Window.partitionBy("vehicle", "mounting_position")
    .orderBy(col("sample_time").cast("long"))
    .rangeBetween(-30 * 60, 0)
)
