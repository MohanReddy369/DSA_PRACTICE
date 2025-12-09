class Sort012{
    // Method to sort 0s, 1s, 2s
    public void sort012(int[] arr) {
        int index=0, count0=0, count1=0, count2=0;

        for(int i=0;i<arr.length;i++){
            //count number of 0s
            if(arr[i]==0) {
                count0++;
            }
            //count number of 1s
            else if(arr[i]==1){
                 count1++;
            }
            //count number of 2s
             else if(arr[i]==2){
                 count2++;
            }
        }
        //fill 0s
        for(int i=0;i<count0;i++){
            arr[index]=0;
            index++;
        }
        //fill 1s
        for(int i=0;i<count1;i++){
            arr[index]=1;
            index++;
        }
        //fill 2s
        for(int i=0;i<count2;i++){
            arr[index]=2;
            index++;
        }
    }

    // Main method to run the program
        public static void main(String[] args) {
        int[] arr = {0, 2, 1, 2, 0, 1};
        Sort012 obj = new Sort012();  // create object
        obj.sort012(arr);              // call method

        // Print sorted array
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
    }
}
