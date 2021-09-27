package ir.aut;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class File_W {

    BufferedWriter writer;

    public File_W(String pathFile) throws IOException {
        writer = new BufferedWriter(new FileWriter(pathFile));
    }

    public void write_to_file(String content) throws IOException {
        writer.write(content);
    }

    public void close_file() throws IOException {
        writer.close();
    }
} 