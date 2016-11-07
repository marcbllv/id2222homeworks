import java.io.FileReader;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.IOException;

import java.util.ArrayList;

class Shingling {
    private int k;

    Shingling(int k) {
        this.k = k;
    }

    ArrayList<String> shingles(String filename) {
        Reader r = null;

        try {
            r = new BufferedReader(new FileReader(filename));
            String str = "";
            int rd;

            while((rd = r.read()) != -1) {
                char c = (char)rd;
                str += c;
                System.out.println(str);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (r != null) r.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return null;
    }
}
