import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

public class Matchup {
    
    // private Scanner scanner = new Scanner(System.in);
    public filePath path = new filePath();
    private String dir = path.dir;

    public Matchup() {
        addGames();
        predict();
    }

    private void addGames() {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", dir + "src/python/oddsScraper.py");
            processBuilder.environment().put("PYTHONPATH", dir + ".venv/Lib/site-packages");

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
