package matriz;

public class Matrix {


    public static void print(int[][] matriz) {
        for (int i = 0; i < matriz.length;i++){
            for (int j = 0; j<matriz[0].length;j++){
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
        
    public static boolean haveSameDimension(int[][] matriz1, int[][] matriz2){
        return false;
    
    }
        
    public static int[][] add(int[][] matriz1, int[][] matriz2){
        return null;

    }

    public static int[][] substract(int[][] matriz1, int[][] matriz2) {
        return null;
    
    }
        
    public static int[][] multiply(int[][] matriz1, int[][] matriz2) {
        return null;
    }

        

    public static void main(String[] args) {
        int[][] matriz1 = {{1,1,1},{2,2,2},{3,3,3}};
        int[][] matriz2 = {{0,0,0},{4,4,4},{5,5,5}};
        print(matriz1);
        print(matriz2);

    }
}
