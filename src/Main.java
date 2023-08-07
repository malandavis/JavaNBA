import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Welcome to the NBA Matchup Predictor!");
        while (true) {
            System.out.println("Select one of the following options:");
            System.out.println("1. Predict Matchup");
            System.out.println("2. Add Results");
            System.out.println("3. Get Model Statistics");
            System.out.println("4. Lookup a Team's Statistics");
            System.out.println("5. Exit");

            Scanner scanner = new Scanner(System.in);
            int option = scanner.nextInt();     //reads in user input
            scanner.nextLine();
            switch (option) {
                case 1:     // Predict Matchup
                    System.out.println("Is this a new day? (Y/n): ");
                    String newDay = scanner.nextLine();
                    new Matchup(newDay);
                    break;
                case 2:   // Add Results
                    new AddResults();
                    break;
                case 3:     // Get Model Statistics
                    new Results();
                    break;
                case 4:     // Lookup a Team's Statistics
                    new Team();
                    break;
                case 5:     // Exit
                    System.out.println("Exiting . . . ");
                    System.exit(0);
                    scanner.close();
                    break;
                default:
                    System.out.println("Invalid option selected");
                    break;
            }
        }
	}
}
