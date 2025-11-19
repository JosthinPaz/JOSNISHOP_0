ALTER TABLE pagos 
    MODIFY COLUMN nombre_tarjeta VARCHAR(255) NOT NULL,
    MODIFY COLUMN numero_tarjeta VARCHAR(255) NOT NULL,
    MODIFY COLUMN fecha_expiracion VARCHAR(255) NOT NULL,
    MODIFY COLUMN cvv VARCHAR(255) NOT NULL;

-- Agregar columnas faltantes que el modelo espera (si no existen)
ALTER TABLE pagos
    ADD COLUMN IF NOT EXISTS tipo_pago VARCHAR(50) DEFAULT 'tarjeta_credito',
    ADD COLUMN IF NOT EXISTS tipo_tarjeta VARCHAR(50) DEFAULT 'unknown',
    ADD COLUMN IF NOT EXISTS referencia_pago VARCHAR(255) DEFAULT NULL,
    ADD COLUMN IF NOT EXISTS banco VARCHAR(100) DEFAULT NULL,
    ADD COLUMN IF NOT EXISTS monto INT DEFAULT 0,
    ADD COLUMN IF NOT EXISTS estado VARCHAR(50) DEFAULT 'completado';