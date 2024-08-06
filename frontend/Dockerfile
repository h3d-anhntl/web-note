# Sử dụng image Node.js
FROM node:18

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép package.json và cài đặt các phụ thuộc
COPY package*.json ./
RUN npm install

# Sao chép toàn bộ mã nguồn vào container
COPY . .

RUN npm run build

# Khởi động ứng dụng React
CMD ["npm","run", "preview"]