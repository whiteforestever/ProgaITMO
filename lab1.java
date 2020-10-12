public class proga_01{

	public static void main(String[] args){
		
		int i;
		final int a = -7, b = 3;
		int j = 18;
		double[] x = new double[11];
		long[] c = new long[8];
		double[][] v = new double[8][11];

		for(i = 0; i < 8; ++i){	
			c[i] = j;
			j-= 2;
		}

		for(i = 0; i < 11; ++i){
			x[i] = ((Math.random() * (b-a)) + a);
		}
		
		for(i = 0; i < 8; ++i){
			for(j = 0; j < 11; ++j){
				if(c[i] == 12){
					v[i][j] = Math.atan(Math.pow (Math.E, -(Math.abs (x[j])))) - 1;
				}
				else if(c[i] == 6 || c[i] == 10  || c[i] == 16 || c[i] == 18){
					v[i][j] = Math.asin(Math.sin(Math.asin( (x[j]-2)/1*Math.E+1)));
				}
				else{
					v[i][j] = Math.tan( Math.tan(Math.pow(Math.tan(x[j]), 1.0/3)));
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
