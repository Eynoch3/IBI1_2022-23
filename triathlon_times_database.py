class triathlon:
  def __init__(self,a,b,c,d,e):
   self.a=a # store the person's firt name and sencond name
   self.b=b #store the location at which the competition took place
   self.c=c #store the person's time for swim
   self.d=d #store the person's time for cycle
   self.e=e #store the person's time for run
  def print_result(self):
   print ('name:',self.a,'/location:',self.b,'/the time for swim:',self.c,'/the time for cycle:',self.d,'/the time for run:',self.e,'/the total time over the triathlon:',self.c+self.d+self.e)

athelet=triathlon('Nanthan Hale','Paris',32.5,66.5,42.8)
athelet.print_result()
