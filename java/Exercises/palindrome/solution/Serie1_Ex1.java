
/**
 * Write a description of class Serie1_Ex1 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Serie1_Ex1
{
    public static void main (String[] args){
        String str = "engage le jeu que je le gagne";
        if (isPalindrome (str)){
            System.out.println (str + " est un palindrome");
        }
    }

    public static String clean(String s){
        String clean = "";
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i)!=' '){
                clean+=s.charAt(i);
            }
        }
        return clean;
    }

    public static boolean isPalindrome (String s){
        String d = clean(s);
        for (int i=0; i<=d.length()-i; i++){
            if(d.charAt(i)!=d.charAt(d.length()-i)){
                return false;
            }
        }
        return true;
    }
}

