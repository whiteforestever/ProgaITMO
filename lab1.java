public class proba{

	public static void main(String[] args){
		
int i;
final int a = -7, b = 3;
int j = 18;
long[] d = new long[8];
double[] x = new double[11];
double[][] v = new double[8][11];

for(i = 0; i < 8; ++i){	
	d[i] = j;
	j-= 2;
}

for(i = 0; i < 11; ++i){
	x[i] = ((Math.random() * (b-a)) + a);
}

for(i = 0; i  <8; ++i){
	for(j = 0; j < 11; ++j){
		if(d[i] == 12){
			v[i][j] = Math.atan(Math.pow(Math.E, -(Math.abs (x[i])))) - 1;
		}
		else if(d[i] == 6 || d[i] == 10  || d[i] == 16 || d[i] == 18){
			v[i][j] = Math.asin(Math.sin(Math.asin( (x[i]-2)/1*Math.E+1) ));
		}
		else{
			v[i][j] = Math.tan( Math.tan(Math.pow(Math.tan(x[i]), 1.0/3)));
		}
	}
}

for(i = 0; i < 8; ++i){
	for(j = 0; j < 11; ++j){
		System.out.printf("%.4f\t", v[i][j]);
	}
System.out.print("\n");
}

	}

}
