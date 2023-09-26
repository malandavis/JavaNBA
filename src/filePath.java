public class filePath {

    public String dir = path();

    filePath() {
        
    }

    public String path() {
        if (System.getProperty("user.dir").contains("src")) {
            return "../";
        }
        else {
            return "";
        }
    }


}
