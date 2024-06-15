-- This script  creates an index idx_name_first on the table names and the first letter of name.

CREATE INDEX inx_name_first ON names (name(1));
