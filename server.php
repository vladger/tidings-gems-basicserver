<?php
// Define the required parameter
$requiredParam = 'm';

// Log the request method and headers for debugging
error_log('Request Method: ' . $_SERVER['REQUEST_METHOD']);
error_log('Request Headers: ' . print_r(getallheaders(), true));

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Log the raw request body for debugging
    $requestBody = file_get_contents('php://input');
    error_log('Raw Request Body: ' . $requestBody);

    // Parse the raw request body into an associative array
    parse_str($requestBody, $requestData);

    // Log the parsed request data for debugging
    error_log('Parsed Request Data: ' . print_r($requestData, true));

    // Check if the required parameter exists
    if (isset($requestData[$requiredParam])) {
        // Determine which action to perform based on the value of 'm'
        $action = $requestData[$requiredParam];

        switch ($action) {
            case 'auth':
            case 'getVipScore':
                // Respond with the corresponding JavaScript file
                $filePath = __DIR__ . '/' . $action . '.js';
                if (file_exists($filePath)) {
                    header('Content-Type: application/javascript');
                    readfile($filePath);
                    exit;
                } else {
                    http_response_code(404);
                    echo 'File not found for action: ' . $action;
                    exit;
                }
                break;

            case 'levelGet':
                // Check if the 'l' parameter exists
                if (isset($requestData['l'])) {
                    // Determine the level file to load based on the 'l' parameter
                    $level = $requestData['l'];
                    $filePath = __DIR__ . '/levels/' . $level . '.js';

                    if (file_exists($filePath)) {
                        header('Content-Type: application/javascript');
                        readfile($filePath);
                        exit;
                    } else {
                        http_response_code(404);
                        echo 'Level file not found: ' . $level;
                        exit;
                    }
                } else {
                    // Respond with a default message if the 'l' parameter is missing
                    http_response_code(400);
                    echo 'Missing required parameter: l';
                    exit;
                }
                break;

            default:
                // Respond with a default message if the action is not supported
                http_response_code(400);
                echo 'Unsupported action: ' . $action;
                exit;
        }
    } else {
        // Respond with a default message if the parameter is missing
        http_response_code(400);
        echo 'Missing required parameter. Available parameters: ' . implode(', ', array_keys($requestData));
        exit;
    }
} else {
    // Respond with an error if the request method is not supported
    http_response_code(405);
    echo 'Method not allowed.';
    exit;
}
?>