    art_type = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
    num_polygons = 30  # You can adjust the number of polygons
    art = PolygonArt(num_polygons, art_type)
    art.run()