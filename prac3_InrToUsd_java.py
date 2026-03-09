from flask import Flask, request, jsonify

app=Flask("RS to $")

@app.route('/convert', methods=['POST'])
def convertion_rs():
   try:
      data = request.get_json()
      amt_rs = data['rs']
      rate = 0.012
      dollar = amt_rs* rate
      return jsonify({"Result":f"Rs{amt_rs} ==> ${format(dollar, '.4f')}"})
   except Exception as e:
      return jsonify({"Error ": str(e)}), 500

if __name__=="__main__":
   app.run(debug=True, port=8796)

#java
import java.net.HttpURLConnection;
import java.net.URL;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStream;

import java.util.Scanner;

public class RsToUsdClient {
   public static void main(String[] args) throws Exception {
      String url = "http://127.0.0.1:8796/convert";
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter a rs amount to convert: ");
      double amtRs = sc.nextDouble();
      String jsonContentString = "{\"rs\":" + amtRs + "}";
      sc.close();

      URL obj = new URL(url);
      HttpURLConnection con = (HttpURLConnection) obj.openConnection();
      con.setRequestMethod("POST");
      con.setRequestProperty("Content-type", "application/json");
      con.setDoOutput(true);

      OutputStream ops = con.getOutputStream();
      ops.write(jsonContentString.getBytes());
      ops.flush();
      ops.close();

      int resCode = con.getResponseCode();
      BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
      String inline;
      StringBuffer response = new StringBuffer();
      while ((inline = br.readLine()) != null) {
         response.append(inline);
      }
      br.close();

      System.out.println("Response code: " + resCode);
      System.out.println("Response: " + response);
   }
}