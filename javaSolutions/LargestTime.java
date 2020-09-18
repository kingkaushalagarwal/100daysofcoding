import java.util.Scanner;
public class LargestTime {
    public static void main(String args[]) {
        LargestTime lt = new LargestTime();
        Solution sol = new Solution();
        int array []= new int[4];
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<4;i++)
            array[i]=sc.nextInt();

        String ans = sol.largestTimeFromDigits(array);
        System.out.println(ans);

    }


    static class Solution {
        private int max_time = -1;

        public String largestTimeFromDigits(int[] arr) {
            this.max_time = -1;
            permutate(arr, 0);
            if (this.max_time == -1)
                return "";
            else
                return String.format("%02d:%02d", max_time / 60, max_time % 60);

        }

        protected void permutate(int[] array, int start) {
            if (start == array.length) {
                this.build_time(array);
                return;
            }
            for (int i = start; i < array.length; i++) {
                this.swap(array, i, start);
                this.permutate(array, start + 1);
                this.swap(array, i, start);
            }
        }

        protected void build_time(int[] perm) {
            int hour = perm[0] * 10 + perm[1];
            int minute = perm[2] * 10 + perm[3];
            if (hour < 24 && minute < 60)
                this.max_time = Math.max(this.max_time, hour * 60 + minute);
        }

        protected void swap(int[] array, int i, int j) {
            if (i != j) {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}