#Compute circumference and Area of a Circle

PI=22/7
radius_inch=float(input('Enter the radius of circle in inches'))
radius_cm=radius_inch * 2.54
circumference_cm=2 * PI * radius_cm
area_square_cm=PI * (radius_cm ** 2)
print(f'\n Circumference of the circle is {circumference_cm:.2f} cm and',
      f'Area of the circle is {area_square_cm:.2f} sqcm')