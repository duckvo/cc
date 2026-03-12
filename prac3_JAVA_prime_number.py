#server
from flask import Flask, request, jsonify

app = Flask("Prime Number Service")

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/prime', methods=['POST'])
def check_prime():
    try:
        data = request.get_json()
        num = data['number']

        if is_prime(num):
            result = f"{num} is a Prime Number"
        else:
            result = f"{num} is NOT a Prime Number"

        return jsonify({"Result": result})

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8796)

#client java
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.util.Scanner;

public class PrimeClient {

    public static void main(String[] args) throws Exception {

        String url = "http://127.0.0.1:8796/prime";

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        sc.close();

        String jsonInput = "{\"number\":" + num + "}";

        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json");
        con.setDoOutput(true);

        OutputStream os = con.getOutputStream();
        os.write(jsonInput.getBytes());
        os.flush();
        os.close();

        int responseCode = con.getResponseCode();

        BufferedReader br = new BufferedReader(
                new InputStreamReader(con.getInputStream()));

        String line;
        StringBuffer response = new StringBuffer();

        while ((line = br.readLine()) != null) {
            response.append(line);
        }

        br.close();

        System.out.println("Response Code: " + responseCode);
        System.out.println("Response: " + response.toString());
    }
}