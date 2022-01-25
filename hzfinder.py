print("Resistor B Value (Ohms)")
rb = input()
print("Capacitor Value (Full Farads)")
c = input()
print("Are you trying to use the reverse formula or the standard formula, put 'reverse' for reverse  and put 'standard' for standard (Standard finds Hz, reverse finds Resistor A)")
reverse = input(str())
while "reverse" in reverse:
  print("Target Hz")
  hz = input()
  m = 1/float(hz)/float(c)/0.7
  r = 2 * float(rb)
  ra = float(m) - float(r)
  print("The resistor you need is approximately ", ra, " Ohms, if this number is negative you must lower the value of Resistor B or the Capacitor to achieve the target Hz")
while "standard" in reverse:
  print("Resistor A Value (Ohms)")
  ra = input()
  rb2 = float(rb) * 2
  i1 = float(ra) + float(rb2)
  i2 = 0.7 * float(i1)
  i3 = float(i2) * float(c)
  out = 1 / float(i3)
  print("The resulting Hz is", out)
