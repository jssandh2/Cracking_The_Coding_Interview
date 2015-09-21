/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String S ,Node root)
    {
        String[] chars = S.split("(?!^)");
        String finalString = "";
        int left = 0;
        String currChar = chars[left];
        int right = chars.length - 1;
        Node temp = null;
        boolean toStop = false;
        while (left <= right && !toStop){
            temp = root;
            while (temp.left != null && temp.right != null){
                if (currChar.equalsIgnoreCase("1")){
                    temp = temp.right;
                }
                else{
                    temp = temp.left;
                }
                if (left != right){
                    left++;    
                }
                else{
                    toStop = true;
                }
                currChar = chars[left];
            }
            finalString += String.valueOf(temp.data);
        }
        System.out.println(finalString);
    }
