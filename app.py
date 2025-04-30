# Trong hàm show_code
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mã Code YeuMoney</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-lg max-w-md w-full text-center">
        <img src="https://your-logo-url.com/logo.png" alt="Logo" class="mx-auto mb-4 h-16">
        <h1 class="text-4xl font-bold mb-4 text-purple-700">Mã Code YeuMoney</h1>
        <p class="text-lg text-gray-600 mb-6">Dưới đây là mã code của bạn:</p>
        <div class="bg-gray-200 p-4 rounded-lg mb-6">
            <p id="code" class="text-2xl font-mono text-purple-800">{{ code }}</p>
        </div>
        <button onclick="copyCode()" class="bg-purple-500 text-white px-6 py-2 rounded-lg hover:bg-purple-600 transition">Sao chép mã</button>
    </div>

    <script>
        function copyCode() {
            const code = document.getElementById('code').innerText;
            navigator.clipboard.writeText(code).then(() => {
                alert('Đã sao chép mã code!');
            });
        }
    </script>
</body>
</html>
""".replace("{{ code }}", code)