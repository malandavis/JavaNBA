import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class TextEditor extends BufferedWriter {

    public TextEditor(String filePath, boolean append) throws IOException {
        super(new FileWriter(filePath, append));
    }

    public static TextEditor open(String filePath, boolean append) throws IOException {
        return new TextEditor(filePath, append);
    }

    // Optionally, you can add convenience methods for writing and closing the file.
    public void writeLine(String line) throws IOException {
        write(line);
        newLine();
    }

    public void closeFile() throws IOException {
        close();
    }
}
