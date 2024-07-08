package org.frontendbackendintegration;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.junit.Assert;
import org.junit.Test;

public class FrontendBackendIntegrationTest {

    @Test
    public void testFrontendBackendIntegration() throws Exception {
        HttpClient client = HttpClientBuilder.create().build();
        // Adjust the URL to match your frontend service access point
        HttpGet request = new HttpGet("http://localhost:30997"); // Use the port-forwarded URL

        HttpResponse response = client.execute(request);

        // Check response status code
        int statusCode = response.getStatusLine().getStatusCode();
        Assert.assertEquals(200, statusCode); // Assert HTTP 200 OK

        // Check response content
        String responseBody = EntityUtils.toString(response.getEntity());
        Assert.assertTrue(responseBody.contains("Hello from the Backend!"));

        // Log success message
        System.out.println("Integration test passed successfully! http://localhost:30997 ");
    }
}
