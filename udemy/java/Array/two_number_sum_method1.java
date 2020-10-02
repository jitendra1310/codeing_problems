/*
Two Number Sum Problem Statement
Given an array of integers, return the indices of the two numbers whose sum is equal to a given target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9.

The output should be [0, 1]. 
Because nums[0] + nums[1] = 2 + 7 = 9.
Time complexity: O(n^2)
*/

import java.util.HashMap;
import java.util.Scanner;
import java.util.Map;

public class two_number_sum_method1 {

    private static int[] findTwoSum_BruteForce(int[] nums, int target ) {
        for(int i = 0; i < nums.length ; i++){
            for(int j = i+1; j < nums.length ; j++ ){                
                if(nums[i]+nums[j] == target){
                    return new int[] {i,j};
                } 
            }
        }
        
        return new int[] {}; 
    }

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        int n = keyboard.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i < n; i++) {
            nums[i] = keyboard.nextInt();
        }
        int target = keyboard.nextInt();

        keyboard.close();

        int[] indices = findTwoSum_BruteForce(nums, target);

        if (indices.length == 2) {
            System.out.println(indices[0] + " " + indices[1]);
        } else {
            System.out.println("No solution found!");
        }
    }
}
