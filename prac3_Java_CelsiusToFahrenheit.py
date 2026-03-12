#server
from flask import Flask, request, jsonify

app = Flask("Fahrenheit to Celsius")

@app.route('/convert', methods=['POST'])
def convert_temp():
    try:
        data = request.get_json()
        fahrenheit = data['fahrenheit']

        celsius = (fahrenheit - 32) * 5/9

        return jsonify({
            "Result": f"{fahrenheit}°F ==> {format(celsius, '.2f')}°C"
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

public class FahrenheitToCelsiusClient {

    public static void main(String[] args) throws Exception {

        String url = "http://127.0.0.1:8796/convert";

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter temperature in Fahrenheit: ");
        double fahrenheit = sc.nextDouble();

        String jsonInput = "{\"fahrenheit\":" + fahrenheit + "}";

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
        System.out.println("Server Response: " + response.toString());

        sc.close();
    }
}