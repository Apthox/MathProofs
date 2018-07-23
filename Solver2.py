import wolframalpha

client = wolframalpha.Client("RRRLTV-GPJLHPE2A4")

request = "solve " \
          "(-d * X1) - (c1 * Y * (X1 / (1 + X1))) + (e ** (-ke * H) * j * (X1 / (1 + X1))) + (l * (X1 / (1 + X1)) * Z)" \
          " and " \
          "(-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * e ** (-ke * H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)" \
          " and " \
          "(-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p * (1 / e ** (-ke * H))) * (Y / (Y + 1)))" \
          " and " \
          "(l * X1) + (f2 * X2) - (m * Z)" \
          " for X1 and X2 and Y and Z"

res = client.query(request)

print(next(res.results).text)