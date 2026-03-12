#server
from flask import Flask, request, jsonify

app = Flask("Factorial Service")

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

@app.route('/factorial', methods=['POST'])
def calculate_factorial():
    try:
        data = request.get_json()
        number = data['number']
        
        result = factorial(number)

        return jsonify({
            "Number": number,
            "Factorial": result
        })

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

public class FactorialClient {

    public static void main(String[] args) throws Exception {

        String url = "http://127.0.0.1:8796/factorial";

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        sc.close();

        String jsonInputString = "{\"number\":" + num + "}";

        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json");
        con.setDoOutput(true);

        OutputStream os = con.getOutputStream();
        os.write(jsonInputString.getBytes());
        os.flush();
        os.close();

        int responseCode = con.getResponseCode();

        BufferedReader br = new BufferedReader(
                new InputStreamReader(con.getInputStream()));

        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = br.readLine()) != null) {
            response.append(inputLine);
        }

        br.close();

        System.out.println("Response Code: " + responseCode);
        System.out.println("Response: " + response.toString());
    }
}