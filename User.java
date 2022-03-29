/**
 *
 * 
 */
public class User {
    ///private String name;
    private String username;
    private String password;
    
    public User() {
        //name = null;
        username = null;
        password = null;
    }
    
    public User(String user, String pass) {
        //name = n;
        username = user;
        password = pass;
    }

    /**
     * @return the username
     */
    public String getUsername() {
        return username;
    }

    /**
     * @param username the username to set
     */
    public void setUsername(String user) {
        this.username = user;
    }

    /**
     * @return the password
     */
    public String getPassword() {
        return password;
    }

    /**
     * @param password the password to set
     */
    public void setPassword(String pass) {
        this.password = pass;
    }
    
    public String toString() {
        return username + "\n" + password;
    }
}
