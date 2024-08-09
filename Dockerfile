# Use the official Odoo image as a base
FROM odoo:17.0

# Create a new directory inside the container
RUN mkdir -p /odoo/extra-addons

# Copy your custom modules into the Odoo addons directory
COPY ./custom_addons /odoo/extra-addons

# Copy your Odoo configuration file
COPY ./odoo.conf /etc/odoo/odoo.conf

# Set the correct permissions
RUN chown -R odoo:odoo /odoo/extra-addons

# Expose Odoo's default port
EXPOSE 8069

# Start Odoo service
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
