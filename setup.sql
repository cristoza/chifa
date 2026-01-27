-- =========================================================
-- SCRIPT DE CONFIGURACIÓN BASE DE DATOS CHIFA
-- =========================================================

-- 1. Creación de Tablas
CREATE TABLE IF NOT EXISTS consultas (
    id SERIAL PRIMARY KEY,
    pregunta_clave VARCHAR(100) NOT NULL,
    respuesta TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS historial_chat (
    id SERIAL PRIMARY KEY,
    ip_usuario VARCHAR(50),
    mensaje_usuario TEXT,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Carga de 50 Preguntas y Respuestas
INSERT INTO consultas (pregunta_clave, respuesta) VALUES 
('hola', '¡Hola! Bienvenido al Chifa. ¿En qué puedo ayudarte hoy? 🥢'),
('menu', 'Tenemos platos personales, familiares y banquetes. ¿Te gustaría ver especialidades o arroces?'),
('carta', 'Puedes ver nuestra carta digital en el local o consultar precios específicos aquí.'),
('chaufa pollo', 'El Arroz Chaufa de Pollo es un clásico al wok con cebollita china. Precio: $18.'),
('chaufa especial', 'Nuestro Chaufa Especial trae pollo, carne y chancho ahumado. ¡El más pedido! Precio: $25.'),
('aeropuerto', 'El Aeropuerto lleva arroz chaufa, tallarín saltado y frijolito chino. Muy contundente.'),
('tipakay', 'El Pollo Tipakay es agridulce, servido con salsa roja y trozos de piña.'),
('chijaukay', 'El Pollo Chijaukay es salado, bañado en salsa de ostión y canela china.'),
('kam lu wantan', 'Festival de sabores: wantanes fritos, carnes, verduras y frutas en salsa agridulce.'),
('wantan frito', 'La porción de 12 unidades viene con nuestra famosa salsa tamarindo. Precio: $12.'),
('sopa wantan', 'Sopa reconfortante con wantanes rellenos, col china y fideos.'),
('tallarin saltado', 'Tallarines con verduras frescas y carne a tu elección (pollo, res o chancho).'),
('chancho agridulce', 'Trozos de chancho crocante con pimientos, piña y salsa agridulce.'),
('lomo saltado', 'Hacemos una versión fusión de lomo saltado con el toque del wok oriental.'),
('delivery', '¡Sí tenemos delivery! El costo depende de tu zona. ¿Me indicas tu dirección?'),
('horario', 'Atendemos de lunes a domingo de 12:00 PM a 10:00 PM.'),
('ubicacion', 'Estamos ubicados en la Av. Principal 123. ¡Te esperamos!'),
('telefono', 'Puedes llamarnos o escribirnos al WhatsApp: 987-654-321.'),
('medios de pago', 'Aceptamos efectivo, tarjetas, Yape y Plin.'),
('yape', '¡Claro que sí! Puedes pagar con Yape al número de contacto.'),
('vegetariano', 'Tenemos opciones como Arroz Chaufa de verduras o Tallarín saltado vegetariano.'),
('picante', 'Prueba nuestro Pollo al curry o pide ají chinero aparte.'),
('banquete', 'Tenemos banquetes para 4, 6 y 10 personas. Ideales para reuniones.'),
('precio chaufa', 'El chaufa personal está desde $15, dependiendo de la carne.'),
('familiar', 'Nuestras fuentes familiares rinden para 3 a 4 personas.'),
('chaufa de carne', 'Arroz chaufa con trozos de lomo de res saltado. Precio: $22.'),
('chaufa de chancho', 'Preparado con chancho asado al estilo oriental.'),
('aeropuerto especial', 'Lleva todas las carnes (pollo, res, chancho) más huevo de codorniz.'),
('sopa wantan especial', 'Trae wantanes, pollo, chancho, pato y verduras.'),
('limonada', 'Tenemos limonada frozen y natural de 1 litro o vaso.'),
('chicha', 'Nuestra chicha morada es casera, preparada con maíz morado.'),
('gaseosa', 'Tenemos Coca-Cola e Inca Kola de 500ml y 1.5L.'),
('postre', 'Te recomendamos nuestro Min Pao dulce o frutas de estación.'),
('min pao', 'Tenemos Min Pao salado (carne) y dulce (frijol colado).'),
('jengibre', 'Muchos platos llevan kion (jengibre) para el sabor auténtico.'),
('sin sal', 'Podemos preparar tus platos con poca sal si lo solicitas.'),
('alergia', 'Por favor avísanos si eres alérgico al maní o mariscos.'),
('mariscos', 'Tenemos chaufa de mariscos y tallarín con langostinos.'),
('arroz blanco', 'También servimos porción de arroz blanco.'),
('tiempo', 'El pedido suele demorar entre 15 a 40 minutos.'),
('recoger', 'Puedes pedir ahora y recoger en el local en 20 minutos.'),
('factura', 'Sí, emitimos boleta y factura electrónica.'),
('estacionamiento', 'Contamos con espacio para clientes frente al local.'),
('reservar', 'Para reservas de más de 8 personas, por favor llámanos.'),
('descuento', 'Los martes tenemos 20% de descuento en el segundo plato.'),
('chaufa de mariscos', 'Mezcla de calamares y langostinos saltados con arroz.'),
('tallarin sam si', 'Tallarín con tres tipos de carnes y verduras selectas.'),
('pollo con verduras', 'Un plato ligero con brócoli, col china y zanahoria.'),
('tausi', 'Pollo al Tausi con el toque salado de frijoles negros fermentados.'),
('gracias', '¡De nada! Fue un placer. ¡Espero tu pedido! 🏮');
