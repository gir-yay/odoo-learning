# Use the official Odoo image as a base
FROM odoo:17.0

# Copy your custom modules into the Odoo addons directory
COPY ./custom_addons /mnt/extra-addons

# Copy your Odoo configuration file
COPY ./odoo.conf /etc/odoo/odoo.conf

# Set the correct permissions
RUN chown -R odoo:odoo /mnt/extra-addons

# Expose Odoo's default port
EXPOSE 8069

# Start Odoo service
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
