import java.util.Scanner;

public class Main {
    static boolean firstRun;

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int option;
        System.out.println("Welcome to the NBA Matchup Predictor!");
        firstRun = true;
        while (true) {
            if (firstRun == false || args.length == 0) { 
                System.out.println("Select one of the following options:");
                System.out.println("1. Predict Matchup");
                System.out.println("2. Add Results");
                System.out.println("3. Get Model Statistics");
                System.out.println("4. Lookup a Team's Statistics");
                System.out.println("5. Exit");
                
                option = scanner.nextInt();     //reads in user input
                scanner.nextLine();
            }
            else {option = Integer.parseInt(args[0]);}
            firstRun = false;
            switch (option) {
                case 1:     // Predict Matchup
                    new Matchup();
                    break;
                case 2:   // Add Results
                    new AddResults();
                    break;
                case 3:     // Get Model Statistics
                    new Statistics();
                    break;
                case 4:     // Lookup a Team's Statistics
                    new Team();
                    break;
                case 5:     // Exit
                    System.out.println("Exiting . . . ");
                    System.exit(0);
                    // scanner.close();
                    break;
                default:
                    System.out.println("Invalid option selected");
                    scanner.close();
                    break;
            }

        }
	}
}
