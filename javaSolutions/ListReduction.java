import java.util.*;
public class ListReduction {
        public static void main(String args[] ) throws Exception {
            int n,k;
            Scanner sc = new Scanner(System.in);
            n = sc.nextInt();
            k = sc.nextInt();
            int arr[] = new int[n];
            PriorityQueue<Integer> pQueueMin = new PriorityQueue<Integer>();
            PriorityQueue<Integer> pQueueMax = new PriorityQueue<Integer>(Collections.reverseOrder());

            for(int i=0;i<n;i++)
            {
                arr[i]=sc.nextInt();
                pQueueMin.add(arr[i]);
                pQueueMax.add(arr[i]);
            }
            int maxx,minn;
            for(int j=0;j<k;j++)
            {   maxx = pQueueMax.poll();
                minn = pQueueMin.poll();
                pQueueMax.remove(minn);
                pQueueMin.remove(maxx);
                if (Math.floor(maxx/2)<=minn)
                {   pQueueMax.add(maxx);
                    pQueueMax.add(minn);
                    pQueueMin.add(maxx);
                    pQueueMin.add(minn);
                    break;

                }
                maxx = (int) Math.ceil(maxx/2);
                minn = minn*2;
                System.out.println(minn+" "+maxx);
                pQueueMax.add(maxx);
                pQueueMax.add(minn);
                pQueueMin.add(maxx);
                pQueueMin.add(minn);

            }
            int summ=0;

            Iterator<Integer> itr3 = pQueueMax.iterator();
            while (itr3.hasNext()) {
                int val= (int) itr3.next();
                System.out.println(val);
                summ+=val;
            }
            System.out.println(summ);



        }
    }

