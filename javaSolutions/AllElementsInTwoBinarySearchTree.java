import java.util.ArrayList;
import java.util.List;

public class AllElementsInTwoBinarySearchTree {
    static class Solution {

        protected static void inorder(TreeNode root, List<Integer> l){
            if (root==null)
                return;
            inorder(root.left,l);
            l.add(root.val);
            inorder(root.right,l);
        }
        public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
            List<Integer> l1 = new ArrayList();
            List<Integer> l2 = new ArrayList();
            inorder(root1,l1);
            inorder(root2,l2);
            List<Integer> ans = new ArrayList();
            int i=0,j=0;
            while(i<l1.size() && j<l2.size()){

                if (l1.get(i)<l2.get(j)){
                    ans.add(l1.get(i));
                    i+=1;
                }
                else{
                    ans.add(l2.get(j));
                    j+=1;
                }

            }
            while(i<l1.size()){
                ans.add(l1.get(i));
                i+=1;
            }
            while(j<l2.size()){
                ans.add(l2.get(j));
                j+=1;
            }
            return ans;


        }
    }
}
