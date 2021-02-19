import { createRequire } from 'module';
const require = createRequire(import.meta.url);

const { Pool } = require('pg')

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'ip_db',
  password: 'postgres',
  port: 5432,
})

const query = (text, params) => pool.query(text, params)

export default query