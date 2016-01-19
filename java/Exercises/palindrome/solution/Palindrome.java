// Palindrome.java

/**
 * Programme qui teste si une chaine de caractères est un palindrome
 * 
 * @author Louis Bokiau
 * @author Sébastien Combéfis
 * @version January 19, 2016
 */
public class Palindrome
{
	private static String clean (String s)
	{
		String clean = "";
		for (int i = 0; i < s.length(); i++)
		{
			if (s.charAt (i) != ' ')
			{
				clean += s.charAt (i);
			}
		}
		return clean;
	}
	
	public static boolean isPalindrome (String s)
	{
		String d = clean (s);
		for (int i = 0; i <= d.length() - i; i++)
		{
			if (d.charAt (i) != d.charAt (d.length() - i))
			{
				return false;
			}
		}
		return true;
	}
	
	public static void main (String[] args)
	{
		String str = "engage le jeu que je le gagne";
		if (isPalindrome (str))
		{
			System.out.println ("'" + str + "' est un palindrome.");
		}
	}
}