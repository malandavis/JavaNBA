import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

public class Matchup {
    
    // private Scanner scanner = new Scanner(System.in);
    private filePath path = new filePath();
    private String dir = path.dir;

    public Matchup() {
        predict();
    }

    /// No longer used, but leaving in case

    // private void clearGames() { 
    //     try {
    //         TextEditor file = TextEditor.open(dir + "lib/Games/Games.txt", false);

    //         file.closeFile();

    //     } catch (Exception e) {
    //         System.out.println("Error: " + e.getMessage());
    //     }
    // }

    // private void addGames() {
    //     System.out.println("How many games will be played today? ");
    //     int games = scanner.nextInt();
    //     scanner.nextLine();

    //     try {
    //         TextEditor file = TextEditor.open(dir + "lib/Games/Games.txt", true);

    //         for (int i = 0; i < games; i++) {
    //             System.out.println("Enter the home team: ");
    //             String homeTeam = scanner.nextLine();
    //             System.out.println("Enter the away team: ");
    //             String awayTeam = scanner.nextLine();
    //             System.out.println("Enter the home team's spread: ");
    //             int spread = scanner.nextInt();
    //             scanner.nextLine();
    //             System.out.println("Enter the OU: ");
    //             int OU = scanner.nextInt();
    //             scanner.nextLine();
    //             file.writeLine(homeTeam + "," + awayTeam + "," + spread + "," + OU);
    //         }

    //         file.closeFile();

    //     } catch (Exception e) {
    //         System.out.println("Error: " + e.getMessage());
    //     }
        
    // }

    private void predict() {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", dir + "src/python/predictor.py");
            Process process = processBuilder.start();
            
            InputStream inputStream = process.getInputStream();
            Scanner scanner = new Scanner(inputStream);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println("Python output: " + line);
            }
            scanner.close();
            
            int exitCode = process.waitFor();
            System.out.println("Python script exited with code: " + exitCode);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
