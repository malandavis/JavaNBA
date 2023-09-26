import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

public class Tester {
    public filePath path = new filePath();
    private String dir = path.dir;

    public Tester() {
        Test();
    }

    private void Test() {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", dir + "TestData/src/tester.py");
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
